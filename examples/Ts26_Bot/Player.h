#pragma once

#include "Module.h"
#include <mutex>

class Player : public Module
{
public:
    Player();

    void on_send(const std::vector<std::string>& packet_splitted) override;
    void on_recv(const std::vector<std::string>& packet_splitted) override;

    int get_x();
    int get_y();
    int get_id();
    int get_map_id();

private:
    void handle_at(const std::vector<std::string>& packet_splitted);
    void handle_walk(const std::vector<std::string>& packet_splitted);
    void handle_cinfo(const std::vector<std::string>& packet_splitted);

    int x;
    int y;
    int id;
    int map_id;

    std::mutex mtx;
};

