#pragma once

#include "Module.h"
#include <unordered_map>
#include <utility>
#include <algorithm>

class Scene : public Module
{
public:
    void on_recv(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    std::pair<int, int> get_central_player_position();

private:
    void handle_in(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void handle_mv(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void handle_cmap(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void handle_su(const std::vector<std::string>& packet_splitted, const std::string& full_packet);

    std::unordered_map<int /* id */, std::pair<int, int> /* position */> players;
};

