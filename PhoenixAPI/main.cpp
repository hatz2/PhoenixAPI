/*********************************************************************
 * @file   main.cpp
 * @brief  Packetlogger example using the API
 * 
 * @author Hatz
 * @date   December 2021
 *********************************************************************/

#include <iostream>
#include <nlohmann/json.hpp>
#include "Api.h"

int main()
{
    using json = nlohmann::json;

    std::vector<int> ports = Phoenix::find_ports();

    if (ports.size() <= 0)
    {
        std::cerr << "Find ports failed\n";
        return -1;
    }

    Phoenix::Api api(ports.front());
    
    while (true)
    {
        while (!api.empty())
        {
            std::string message = api.get_message();

            try
            {
                json json_msg = json::parse(message);

                if (json_msg["type"] == Phoenix::Type::packet_send)
                {
                    std::cout << "[SEND]: " << std::string(json_msg["packet"]) << std::endl;
                }

                if (json_msg["type"] == Phoenix::Type::packet_recv)
                {
                    std::cout << "[RECV]: " << std::string(json_msg["packet"]) << std::endl;
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
