#include "Player.h"

Player::Player()
    : x(-1)
    , y(-1)
    , id(-1)
    , map_id(-1)
{
}

void Player::on_send(const std::vector<std::string>& packet_splitted)
{
    std::string header = packet_splitted[0];

    if (header == "walk")
        handle_walk(packet_splitted);
}

void Player::on_recv(const std::vector<std::string>& packet_splitted)
{
    std::string header = packet_splitted[0];

    if (header == "at")
        handle_at(packet_splitted);

    else if (header == "c_info")
        handle_cinfo(packet_splitted);
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

void Player::handle_at(const std::vector<std::string>& packet_splitted)
{
    if (packet_splitted.size() < 9)
        return;

    std::lock_guard<std::mutex> lock(mtx);

    id = std::stoi(packet_splitted[1]);
    map_id = std::stoi(packet_splitted[2]);
    x = std::stoi(packet_splitted[3]);
    y = std::stoi(packet_splitted[4]);
}

void Player::handle_walk(const std::vector<std::string>& packet_splitted)
{
    if (packet_splitted.size() < 5)
        return;

    std::lock_guard<std::mutex> lock(mtx);

    x = std::stoi(packet_splitted[1]);
    y = std::stoi(packet_splitted[2]);
}

void Player::handle_cinfo(const std::vector<std::string>& packet_splitted)
{
    if (packet_splitted.size() < 20)
        return;

    std::lock_guard<std::mutex> lock(mtx);

    id = std::stoi(packet_splitted[6]);
}
