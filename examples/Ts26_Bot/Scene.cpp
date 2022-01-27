#include "Scene.h"

void Scene::on_recv(const std::vector<std::string>& packet_splitted)
{
    std::string header = packet_splitted[0];

    if (header == "in")
        handle_in(packet_splitted);

    else if (header == "out")
        handle_out(packet_splitted);

    else if (header == "su")
        handle_su(packet_splitted);

    else if (header == "drop") 
        handle_drop(packet_splitted);

    else if (header == "get") 
        handle_get(packet_splitted);

    else if (header == "c_map")
        handle_cmap(packet_splitted);
}

size_t Scene::get_monster_count() const
{
    return monsters.size();
}

size_t Scene::get_items_count() const
{
    return items.size();
}

size_t Scene::get_levers_count() const
{
    return levers.size();
}

const std::set<int> Scene::get_items() const
{
    return items;
}

void Scene::handle_in(const std::vector<std::string>& packet_splitted)
{
    if (packet_splitted.size() < 10)
        return;

    int type = std::stoi(packet_splitted[1]);
    int vnum = std::stoi(packet_splitted[2]);
    int id = std::stoi(packet_splitted[3]);

    if (type == 3)
        monsters.emplace(id, vnum);

    if (type == 9)
        levers.emplace(id);
}

void Scene::handle_out(const std::vector<std::string>& packet_splitted)
{
    if (packet_splitted.size() < 3)
        return;

    int id = std::stoi(packet_splitted[2]);

    items.erase(id);
}

void Scene::handle_su(const std::vector<std::string>& packet_splitted)
{
    if (packet_splitted.size() < 13)
        return;

    int id = std::stoi(packet_splitted[4]);
    int type = std::stoi(packet_splitted[3]);
    int hp = std::stoi(packet_splitted[12]);

    if (type == 3 && hp == 0)
        monsters.erase(id);
}

void Scene::handle_drop(const std::vector<std::string>& packet_splitted)
{
    if (packet_splitted.size() < 8)
        return;

    int id = std::stoi(packet_splitted[2]);

    items.emplace(id);
}

void Scene::handle_get(const std::vector<std::string>& packet_splitted)
{
    if (packet_splitted.size() < 5)
        return;

    int id = std::stoi(packet_splitted[3]);

    items.erase(id);
}

void Scene::handle_cmap(const std::vector<std::string>& packet_splitted)
{
    monsters.clear();
    items.clear();
    levers.clear();
}
