#include <iostream>
#include <vector>
#include <mutex>
#include "PhoenixApi/Api.h"
#include "Bot.h"
#include "Scene.h"
#include "Split_string.h"
#include "Logger.h"
#include <sstream>

int select_port();

class RunningBot {
public:
    RunningBot(int port) : port(port) {
        scene = new Scene;
        api = new Phoenix::Api(port);
        bot = new Bot(api, scene);
        modules.push_back(scene);
        modules.push_back(bot);
    }

    ~RunningBot() {
        modules.clear();
        delete bot;
        delete scene;
        delete api;
    }

    void update() {
        if (!api->empty())
        {
            std::string message = api->get_message();

            try
            {
                nlohmann::json json_msg = nlohmann::json::parse(message);

                if (json_msg["type"] == Phoenix::Type::packet_send)
                {
                    std::string packet = json_msg["packet"];
                    std::vector<std::string> packet_splitted = split_string(packet);

                    if (packet_splitted.size() > 0)
                    {
                        for (auto mod : modules)
                            mod->on_send(packet_splitted, packet);
                    }
                }

                if (json_msg["type"] == Phoenix::Type::packet_recv)
                {
                    std::string packet = json_msg["packet"];
                    std::vector<std::string> packet_splitted = split_string(packet);

                    if (packet_splitted.size() > 0)
                    {
                        for (auto mod : modules)
                            mod->on_recv(packet_splitted, packet);
                    }
                }

                if (json_msg["type"] == Phoenix::Type::query_map_entities)
                {
                    bot->handle_map_entities(json_msg);
                }
            }
            catch (const std::exception& e)
            {
                std::stringstream ss;
                ss << "[" << port << "]: " << e.what() << std::endl;
                Logger::error(ss.str());
                return;
            }
        }
        else
        {
            std::this_thread::sleep_for(std::chrono::milliseconds(1));
        }

        bot->run();
    }

private:
    int port;
    Phoenix::Api* api;
    Bot* bot;
    Scene* scene;
    std::vector<Module*> modules;
};

void run_bot(int port)
{
    Phoenix::Api api(port);
    Scene scene;
    Bot bot(&api, &scene);
    std::vector<Module*> modules = { &scene, &bot };

    std::stringstream ss;
    ss << "[" << port << "] Bot is running..." << std::endl;
    Logger::print(ss.str());

    while (true)
    {
        if (!api.empty())
        {
            std::string message = api.get_message();

            try
            {
                nlohmann::json json_msg = nlohmann::json::parse(message);

                if (json_msg["type"] == Phoenix::Type::packet_send)
                {
                    std::string packet = json_msg["packet"];
                    std::vector<std::string> packet_splitted = split_string(packet);

                    if (packet_splitted.size() > 0)
                    {
                        for (auto mod : modules)
                            mod->on_send(packet_splitted, packet);
                    }
                }

                if (json_msg["type"] == Phoenix::Type::packet_recv)
                {
                    std::string packet = json_msg["packet"];
                    std::vector<std::string> packet_splitted = split_string(packet);

                    if (packet_splitted.size() > 0)
                    {
                        for (auto mod : modules)
                            mod->on_recv(packet_splitted, packet);
                    }
                }

                if (json_msg["type"] == Phoenix::Type::query_map_entities)
                {
                    bot.handle_map_entities(json_msg);
                }
            }
            catch (const std::exception& e)
            {
                ss.clear();
                ss << "[" << port << "]: " << e.what() << std::endl;
                Logger::error(ss.str());
                return;
            }
        }
        else
        {
            std::this_thread::sleep_for(std::chrono::milliseconds(10));
        }

        bot.run();
    }
}

int main()
{
    int selected_port = select_port();

    if (selected_port == -1)
        return 0;

    if (selected_port == 0)
    {
        std::vector<int> ports = Phoenix::find_ports();
        std::vector<std::thread> bots;

        for (int port : ports)
            bots.push_back(std::thread(run_bot, port));

        for (auto& bot : bots)
            if (bot.joinable()) bot.join();
    }
    else
    {
        run_bot(selected_port);
    }

    return 0;
}

//int main()
//{
//    int selected_port = select_port();
//
//    if (selected_port == -1)
//        return 0;
//
//    if (selected_port == 0)
//    {
//        std::vector<int> ports = Phoenix::find_ports();
//        std::vector<RunningBot*> bots;
//
//        for (const int port : ports) {
//            RunningBot* bot = new RunningBot(port);
//            bots.push_back(bot);
//        }
//
//        while (true) {
//            for (const auto& bot : bots) {
//                bot->update();
//            }
//        }
//
//        for (auto& bot : bots) {
//            delete bot;
//        }
//    }
//    else
//    {
//        run_bot(selected_port);
//    }
//
//    return 0;
//}

int select_port()
{
    int option = -1;
    int port = -1;

    std::vector<int> ports = Phoenix::find_ports();

    std::cout << "Select the port to connect (-1 to exit):" << std::endl;

    std::cout << "0) Select all" << std::endl;

    for (size_t i = 0; i < ports.size(); ++i)
    {
        std::cout << i + 1 << ") " << ports[i] << std::endl;
    }

    while (true)
    {
        std::cin >> option;

        if (option == -1)
        {
            std::cout << "Exiting..." << std::endl;
            break;
        }

        if (option == 0)
        {
            std::cout << "All ports selected" << std::endl;
            return 0;
        }

        else if (option < 0 || option > (int)ports.size())
        {
            std::cout << "Selected option is not valid, try again." << std::endl;
            std::cout << "Available options are: ";

            std::cout << "0 ";
            for (size_t i = 0; i < ports.size(); ++i)
            {
                std::cout << i + 1 << " ";
            }

            std::cout << std::endl;
        }

        else
        {
            port = ports[option - 1];
            break;
        }
    }

    return port;
}
