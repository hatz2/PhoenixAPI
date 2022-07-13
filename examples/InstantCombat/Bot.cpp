#include "Bot.h"

Bot::Bot(Phoenix::Api* api, Scene* scene)
    : api(api)
    , scene(scene)
    , point({ 0, 0 })
    , round(0)
    , afk_last_round(true)
    , move_to_players(true)
    , move_to_point(false)
    , moving(false)
{
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
}

void Bot::handle_qnamli(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() < 7)
        return;

    if (packet_splitted[2] == "#guri^506" && packet_splitted[3] == "379")
    {
        Logger::print("Joining instant combat\n");

        api->send_packet("guri 508");
        api->send_packet(packet_splitted[2]);
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

        moving = true;
        api->stop_bot();
        ++round;
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

        if (map_id == ic_map_id)
        {
            moving = true;
        }
        else
        {
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

void Bot::run()
{
    static clock_t time_begin = clock();

    if (moving)
    {
        float time_diff = float(clock() - time_begin) / CLOCKS_PER_SEC;

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
