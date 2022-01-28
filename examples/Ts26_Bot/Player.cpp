#include "Player.h"

Player::Player()
    : x(-1)
    , y(-1)
    , id(-1)
    , map_id(-1)
{
}

void Player::on_send(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    std::string header = packet_splitted[0];

    if (header == "walk")
        handle_walk(packet_splitted, full_packet);
}

void Player::on_recv(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    std::string header = packet_splitted[0];

    if (header == "at")
        handle_at(packet_splitted, full_packet);

    else if (header == "c_info")
        handle_cinfo(packet_splitted, full_packet);
}

int Player::get_x()
{
    std::lock_guard<std::mutex> lock(mtx);
    return x;
}

int Player::get_y()
{
    std::lock_guard<std::mutex> lock(mtx);
    return y;
}

int Player::get_id()
{
    std::lock_guard<std::mutex> lock(mtx);
    return id;
}

int Player::get_map_id()
{
    std::lock_guard<std::mutex> lock(mtx);
    return map_id;
}

void Player::handle_at(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() < 9)
        return;

    std::lock_guard<std::mutex> lock(mtx);

    try
    {
        id = std::stoi(packet_splitted[1]);
        map_id = std::stoi(packet_splitted[2]);
        x = std::stoi(packet_splitted[3]);
        y = std::stoi(packet_splitted[4]);
    }

    catch (const std::exception& e)
    {
        std::cerr << "Player::handle_at " << e.what() << std::endl;
        std::cerr << "Packet: " << full_packet << std::endl;
    }
}

void Player::handle_walk(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() < 5)
        return;

    std::lock_guard<std::mutex> lock(mtx);

    try
    {
        x = std::stoi(packet_splitted[1]);
        y = std::stoi(packet_splitted[2]);
    }

    catch (const std::exception& e)
    {
        std::cerr << "Player::handle_walk " << e.what() << std::endl;
        std::cerr << "Packet: " << full_packet << std::endl;
    }
}

void Player::handle_cinfo(const std::vector<std::string>& packet_splitted, const std::string& full_packet)
{
    if (packet_splitted.size() < 20)
        return;

    std::lock_guard<std::mutex> lock(mtx);

    try
    {
        id = std::stoi(packet_splitted[6]);
    }

    catch (const std::exception& e)
    {
        std::cerr << "Player::handle_cinfo " << e.what() << std::endl;
        std::cerr << "Packet: " << full_packet << std::endl;
    }
}
