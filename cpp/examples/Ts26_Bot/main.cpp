#include "PhoenixApi/Api.h"
#include "Split_string.h"
#include "Player.h"
#include "Scene.h"
#include "Bot.h"
#include <iostream>
#include <vector>

int select_port();

int main()
{
    int port = select_port();

    if (port == -1)
        return 0;

    Phoenix::Api api(port);
    Player player;
    Scene scene;
    Bot bot(&api, &player, &scene);
    std::vector<Module*> modules = { &player, &scene, &bot };

    std::cout << "Bot is running..." << std::endl;

    while (true)
    {
        while (!api.empty())
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
                        {
                            mod->on_send(packet_splitted, packet);
                        }
                    }
                }

                if (json_msg["type"] == Phoenix::Type::packet_recv)
                {
                    std::string packet = json_msg["packet"];
                    std::vector<std::string> packet_splitted = split_string(packet);

                    if (packet_splitted.size() > 0)
                    {
                        for (auto mod : modules)
                        {
                            mod->on_recv(packet_splitted, packet);
                        }
                    }
                }
            }

            catch (const std::exception& e)
            {
                std::cerr << e.what() << std::endl;
                std::cin.get();
                return 1;
            }
        }

        std::this_thread::sleep_for(std::chrono::milliseconds(10));
    }


}

int select_port()
{
    int option = -1;
    int port = -1;

    std::vector<int> ports = Phoenix::find_ports();

    std::cout << "Select the port to connect (-1 to exit):" << std::endl;

    for (size_t i = 0; i < ports.size(); ++i)
    {
        std::cout << i << ") " << ports[i] << std::endl;
    }

    while (true)
    {
        std::cin >> option;

        if (option == -1)
        {
            std::cout << "Exiting..." << std::endl;
            break;
        }

        else if (option < 0 || option >= (int)ports.size())
        {
            std::cout << "Selected option is not valid, try again." << std::endl;
            std::cout << "Options are: ";

            for (size_t i = 0; i < ports.size(); ++i)
            {
                std::cout << i << " ";
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
