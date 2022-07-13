#include <iostream>
#include <vector>
#include <mutex>
#include "PhoenixApi/Api.h"
#include "Bot.h"
#include "Scene.h"
#include "Split_string.h"
#include "Logger.h"

int select_port();

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
            port = ports[option];
            break;
        }
    }

    return port;
}
