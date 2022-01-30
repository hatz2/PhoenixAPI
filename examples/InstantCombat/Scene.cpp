#include "Scene.h"

void Scene::on_recv(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    std::string header = packet_splitted[0];

    if (header == "in")
        handle_in(packet_splitted, full_packet);

    if (header == "mv")
        handle_mv(packet_splitted, full_packet);

    if (header == "c_map")
        handle_cmap(packet_splitted, full_packet);

    if (header == "su")
        handle_su(packet_splitted, full_packet);
}

std::pair<int, int> Scene::get_central_player_position()
{
    if (players.size() == 0)
        return { 0, 0 };

    std::vector<int> x_pos;
    std::vector<int> y_pos;

    for (const auto& player : players)
    {
        x_pos.push_back(player.second.first);
        y_pos.push_back(player.second.second);
    }

    std::sort(x_pos.begin(), x_pos.end());
    std::sort(y_pos.begin(), y_pos.end());

    size_t index = players.size() / 2;

    return { x_pos[index], y_pos[index] };
}

void Scene::handle_in(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() < 10)
        return;

    if (packet_splitted[1] != "1")
        return;

    int id;
    int x;
    int y;

    try
    {
        id = std::stoi(packet_splitted[4]);
        x = std::stoi(packet_splitted[5]);
        y = std::stoi(packet_splitted[6]);

        players[id] = { x, y };
    }
    catch (const std::exception& e)
    {
        std::cerr << "Scene::handle_in " << e.what() << std::endl;
        std::cerr << "Packet: " << full_packet << std::endl;
    }
}

void Scene::handle_mv(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() < 6)
        return;

    if (packet_splitted[1] != "1")
        return;

    int id;
    int x;
    int y;

    try
    {
        id = std::stoi(packet_splitted[2]);
        x = std::stoi(packet_splitted[3]);
        y = std::stoi(packet_splitted[4]);

        players[id] = { x, y };
    }
    catch (const std::exception& e)
    {
        std::cerr << "Scene::handle_mv " << e.what() << std::endl;
        std::cerr << "Packet: " << full_packet << std::endl;
    }
}

void Scene::handle_cmap(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() < 4)
        return;

    players.clear();
}

void Scene::handle_su(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
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

        if (type != 1)
            return;

        if (hp == 0)
            players.erase(id);
    }

    catch (const std::exception& e)
    {
        std::cerr << "Bot::handle_su " << e.what() << std::endl;
        std::cerr << "Packet: " << full_packet << std::endl;
    }
}
