#include "Bot.h"
#include <random>
#include <sstream>
#include <chrono>

Bot::Bot(Phoenix::Api* api, Scene* scene)
    : api(api)
    , scene(scene)
    , point({ 0, 0 })
    , round(0)
    , afk_last_round(true)
    , move_to_players(true)
    , move_to_point(false)
    , moving(false)
    , waiting_for_spawn(false)
    , current_map_id(0)
{
    time_begin = clock();
    generator = std::mt19937(std::chrono::system_clock::now().time_since_epoch().count());
    load_config();
}

void Bot::on_recv(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    std::string header = packet_splitted[0];

    if (header == "qnamli")
        handle_qnamli(packet_splitted, full_packet);

    if (header == "msgi")
        handle_msgi(packet_splitted, full_packet);

    if (header == "c_map")
        handle_cmap(packet_splitted, full_packet);

    if (header == "in")
        handle_in(packet_splitted, full_packet);
}

void Bot::handle_in(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (current_map_id == ic_map_id && waiting_for_spawn) 
    {
        waiting_for_spawn = false;
        
        if (moving)
            moving = false;
    }
}

void Bot::handle_qnamli(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() < 7)
        return;

    if (packet_splitted[2] == "#guri^506" && packet_splitted[3] == "379")
    {
        std::uniform_int_distribution<> dist(1000, 10000);
        int random_delay = dist(generator);

        std::thread([this, random_delay, packet_splitted]() {
            std::stringstream ss;
            ss << "Joining instant combat with " << random_delay << " ms delay" << std::endl;
            Logger::print(ss.str());
            std::this_thread::sleep_for(std::chrono::milliseconds(random_delay));
            api->send_packet("guri 508");
            std::uniform_int_distribution<> d(1000, 2000);
            std::this_thread::sleep_for(std::chrono::milliseconds(d(generator)));
            api->send_packet(packet_splitted[2]); 
        }).detach();
        
    }
}

void Bot::handle_msgi(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() < 8)
        return;

    // Here are the monsters! || Monsters are coming in mase
    if (full_packet == "msgi 0 387 0 0 0 0 0" || full_packet == "msgi 0 384 0 0 0 0 0")
    {
        moving = false;

        if (afk_last_round)
        {
            if (round != 4)
                api->start_bot();
        }
        else
        {
            api->start_bot();
        }
    }

    // Monsters will appear in 40 seconds
    if (full_packet == "msgi 0 1287 4 40 0 0 0")
    {
        std::stringstream ss;
        ss << "Round " << round << " finished" << std::endl;
        Logger::print(ss.str());

        api->stop_bot();
        ++round;

        std::uniform_int_distribution<> dist(1000, 10000);
        int random_delay = dist(generator);

        std::thread([this, random_delay, packet_splitted]() {
            std::this_thread::sleep_for(std::chrono::milliseconds(random_delay));
            moving = true;
        }).detach();


        
    }

    if (full_packet == "msgi 0 383 0 0 0 0 0")
    {
        Logger::print("You've won the instant combat\n");
    }
}

void Bot::handle_cmap(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() < 4)
        return;

    int new_map;
    int map_id;

    try
    {
        new_map = std::stoi(packet_splitted[3]);
        map_id = std::stoi(packet_splitted[2]);

        if (new_map == 0)
            return;

        current_map_id = map_id;

        if (map_id == ic_map_id)
        {
            std::uniform_int_distribution<> dist(1000, 10000);
            int random_delay = dist(generator);

            std::thread([this, random_delay, packet_splitted]() {
                std::this_thread::sleep_for(std::chrono::milliseconds(random_delay));
                moving = true;
            }).detach();

            waiting_for_spawn = true;
        }
        else
        {
            std::cout << "Map is not IC map" << std::endl;
            waiting_for_spawn = false;
            moving = false;
            round = 0;
            api->stop_bot();
        }
    }
    catch (const std::exception& e)
    {
        std::stringstream ss;
        ss << "Bot::handle_cmap " << e.what() << std::endl;
        ss << "Packet: " << full_packet << std::endl;

        Logger::error(ss.str());
    }
}

void Bot::handle_map_entities(const nlohmann::json& data)
{
    // Move to point/players when there are no monsters in the map
    if (current_map_id == ic_map_id && data["monsters"].size() == 0 && !waiting_for_spawn) {
        moving = true;
        waiting_for_spawn = true;
        api->stop_bot();
    }
}

void Bot::run()
{
    float time_diff = float(clock() - time_begin) / CLOCKS_PER_SEC;

    if (moving)
    {
        if (time_diff > 1.0f)
        {
            time_begin = clock();

            if (move_to_players)
            {
                std::pair<int, int> position = scene->get_central_player_position();
                walk(position.first, position.second);
            }
            else if (move_to_point)
            {
                walk(point.first, point.second);
            }
        }
    }
    else 
    {
        if (time_diff > 2.0f && current_map_id == ic_map_id)
        {
            time_begin = clock();
            // Send query to check how many mobs are in the map
            api->query_map_entities();
        }
    }
}

void Bot::walk(int x, int y)
{
    if (x > 0 && y > 0)
    {
        api->player_walk(x, y);
        api->pets_walk(x, y);
    }
}

void Bot::load_config()
{
    INIReader reader("./ic_settings.ini");

    if (reader.ParseError() < 0)
    {
        Logger::error("Can't load ic_settings.ini\n");
        return;
    }

    const std::string section = "Settings";
    afk_last_round = reader.GetBoolean(section, "afk_last_round", true);
    move_to_players = reader.GetBoolean(section, "move_to_players", true);
    move_to_point = reader.GetBoolean(section, "move_to_point", false);
    point = { reader.GetInteger(section, "x", 0), reader.GetInteger(section, "y", 0) };
}
