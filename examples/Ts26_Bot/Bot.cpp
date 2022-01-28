#include "Bot.h"

Bot::Bot(Phoenix::Api* api, Player* player, Scene* scene)
    : map_change(0)
    , garg_spawn(0)
    , lever_pick(0)
    , last_lever_spawn(0)
    , api(api)
    , player(player)
    , scene(scene)
    , target_id(-1)
    , lever_id(-1)
    , run(true)
{
    worker = std::thread(&Bot::work, this);
}

Bot::~Bot()
{
    run = false;

    if (worker.joinable())
        worker.join();
}

void Bot::on_send(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    std::string header = packet_splitted[0];

    std::string test = header.substr(0, 4);

    if (test == "#git")
        handle_git(packet_splitted, full_packet);
}

void Bot::on_recv(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    std::string header = packet_splitted[0];

    if (header == "in")
        handle_in(packet_splitted, full_packet);

    else if (header == "at")
        handle_at(packet_splitted, full_packet);

    else if (header == "su")
        handle_su(packet_splitted, full_packet);

    else if (header == "dlgi")
        handle_dlgi(packet_splitted, full_packet);

    else if (header == "npc_req")
        handle_npc_req(packet_splitted, full_packet);

    else if (header == "sayi")
        handle_sayi(packet_splitted, full_packet);
}

void Bot::handle_in(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() < 10)
        return;

    if (packet_splitted[1] == "1")
        return;

    int type;
    int vnum;
    int id;

    try
    {
        type = std::stoi(packet_splitted[1]);
        vnum = std::stoi(packet_splitted[2]);
        id = std::stoi(packet_splitted[3]);
    }

    catch (const std::exception& e)
    {
        std::cerr << "Bot::handle_in " << e.what() << std::endl;
        std::cerr << "Packet: " << full_packet << std::endl;
    }

    if (type == 3 && vnum == garg_vnum)
    {
        target_id = id;
        garg_spawn.release();
    }

    if (type == 9 && (vnum == lever_vnum || vnum == crystal_vnum))
    {
        lever_id = id;

        if (vnum == crystal_vnum)
            last_lever_spawn.release();
    }
}

void Bot::handle_at(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    target_id = -1;
    lever_id = -1;

    map_change.release();
}

void Bot::handle_su(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() < 13)
        return;

    int id;
    int type;
    int hp;

    try
    {
        id = std::stoi(packet_splitted[4]);
        type = std::stoi(packet_splitted[3]);
        hp = std::stoi(packet_splitted[12]);
    }

    catch (const std::exception& e)
    {
        std::cerr << "Bot::handle_su " << e.what() << std::endl;
        std::cerr << "Packet: " << full_packet << std::endl;
    }

    if (type == 3 && hp == 0 && id == target_id)
        target_id = -1;
}

void Bot::handle_dlgi(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() < 6)
        return;

    std::string accept = packet_splitted[1];

    auto pos = accept.find('^');

    if (accept.substr(0, pos) == "#rstart")
        api->send_packet(accept);
}

void Bot::handle_git(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() > 1)
        return;

    auto pos = packet_splitted[0].find('^');

    int id;

    try
    {
        id = std::stoi(packet_splitted[0].substr(pos + 1));
    }

    catch (const std::exception& e)
    {
        std::cerr << "Bot::handle_git " << e.what() << std::endl;
        std::cerr << "Packet: " << full_packet << std::endl;
    }

    if (id == lever_id)
    {
        lever_id = -1;
        lever_pick.release();
    }
}

void Bot::handle_npc_req(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() < 4)
        return;

    int player_id;
    int id;

    try
    {
        player_id = std::stoi(packet_splitted[2]);
        id = std::stoi(packet_splitted[3]);
    }

    catch (const std::exception& e)
    {
        std::cerr << "Bot::handle_npc_req " << e.what() << std::endl;
        std::cerr << "Packet: " << full_packet << std::endl;
    }

    if (player_id != player->get_id())
        return;

    if (id == 6078 || id == 6081 || id == 6082)
        api->send_packet("n_run 5 0 " + std::to_string(player_id));

    else if (id == 6079)
        api->send_packet("n_run 6 0 1 " + std::to_string(player_id));
}

void Bot::handle_sayi(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() < 10)
        return;

    int entity_id;

    try
    {
        entity_id = std::stoi(packet_splitted[2]);
    }

    catch (const std::exception& e)
    {
        std::cerr << "Bot::handle_sayi " << e.what() << std::endl;
        std::cerr << "Packet: " << full_packet << std::endl;
    }

    if (entity_id != player->get_id() || packet_splitted[3] != "10" || packet_splitted[4] != "94")
        return;

    api->send_packet("preq");
}

void Bot::work()
{
    while (run)
    {
        while (player->get_map_id() == -1 || player->get_map_id() == sunny_meadows_id)
        {
            api->send_packet("wreq");
            std::this_thread::sleep_for(std::chrono::milliseconds(1000));
            api->send_packet("wreq 1");
            std::this_thread::sleep_for(std::chrono::milliseconds(5000));
        }

        if (player->get_map_id() == first_ts_room_id)
        {
            map_change.try_acquire();
            garg_spawn.try_acquire();
            lever_pick.try_acquire();
            last_lever_spawn.try_acquire();
            walk(left_portal.first, left_portal.second);
            map_change.acquire();
            walk(left_portal.first, left_portal.second);
            map_change.acquire();
            complete_room();
            walk(left_portal.first, left_portal.second);
            map_change.acquire();
            complete_room();
            walk(bottom_portal.first, bottom_portal.second);
            map_change.acquire();
            complete_room();
            walk(right_portal.first, right_portal.second);
            map_change.acquire();
            complete_room();
            walk(bottom_portal.first, bottom_portal.second);
            map_change.acquire();
            complete_room();
            walk(right_portal.first, right_portal.second);
            map_change.acquire();

            garg_spawn.try_acquire();
            last_lever_spawn.acquire();
            api->pick_up(lever_id);
            lever_pick.acquire();
            garg_spawn.acquire();
            attack_garg();
            std::this_thread::sleep_for(std::chrono::milliseconds(2000));
            pick_up_items();

            api->send_packet("escape");
            map_change.acquire();
        }
    }
}

void Bot::complete_room()
{
    garg_spawn.acquire();
    attack_garg();
    std::this_thread::sleep_for(std::chrono::milliseconds(2000));
    api->pick_up(lever_id);
    lever_pick.acquire();
    std::this_thread::sleep_for(std::chrono::milliseconds(2000));
    pick_up_items();
}

void Bot::pick_up_items()
{
    while (scene->get_items_count() > 0)
    {
        auto items = scene->get_items();

        int id = 0;

        for (const auto item : items)
        {
            id = item;
            break;
        }

        if (id == 0)
            break;

        else
        {
            api->pick_up(id);
            std::this_thread::sleep_for(std::chrono::milliseconds(500));
        }
    }
}

void Bot::attack_garg()
{
    while (target_id > 0)
    {
        api->attack_monster(target_id);
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }
}

void Bot::walk(int x, int y)
{
    while (player->get_x() != x || player->get_y() != y)
    {
        api->player_walk(x, y);
        api->pets_walk(x, y);
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }
}
