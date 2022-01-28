#include "Scene.h"

void Scene::on_recv(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    std::string header = packet_splitted[0];

    if (header == "out")
        handle_out(packet_splitted, full_packet);

    else if (header == "drop") 
        handle_drop(packet_splitted, full_packet);

    else if (header == "get") 
        handle_get(packet_splitted, full_packet);

    else if (header == "c_map")
        handle_cmap(packet_splitted, full_packet);
}

size_t Scene::get_items_count() const
{
    return items.size();
}

const std::set<int> Scene::get_items() const
{
    return items;
}

void Scene::handle_out(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() < 3)
        return;

    int id;

    try
    {
        id = std::stoi(packet_splitted[2]);
    }

    catch (const std::exception& e)
    {
        std::cerr << "Scene::handle_out " << e.what() << std::endl;
        std::cerr << "Packet: " << full_packet << std::endl;
    }

    items.erase(id);
}

void Scene::handle_drop(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() < 8)
        return;

    int id;

    try
    {
        id = std::stoi(packet_splitted[2]);
    }

    catch (const std::exception& e)
    {
        std::cerr << "Scene::handle_drop " << e.what() << std::endl;
        std::cerr << "Packet: " << full_packet << std::endl;
    }

    items.emplace(id);
}

void Scene::handle_get(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() < 5)
        return;

    int id;

    try
    {
        id = std::stoi(packet_splitted[3]);
    }

    catch (const std::exception& e)
    {
        std::cerr << "Scene::handle_get " << e.what() << std::endl;
        std::cerr << "Packet: " << full_packet << std::endl;
    }

    items.erase(id);
}

void Scene::handle_cmap(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    items.clear();
}
