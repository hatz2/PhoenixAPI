#pragma once
#include "Module.h"
#include "Scene.h"
#include "PhoenixApi/Api.h"
#include <utility>
#include <atomic>
#include <thread>

class Bot : public Module
{
public:
    explicit Bot(Phoenix::Api* api, Scene* scene);

    void on_recv(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void move();

private:
    void handle_qnamli(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void handle_msgi(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void handle_cmap(const std::vector<std::string>& packet_splitted, const std::string& full_packet);

    void walk(int x, int y);
    void load_config();

    static constexpr int ic_map_id = 2004;
    Phoenix::Api* api;
    Scene* scene;
    std::pair<int, int> point;
    int round;
    bool afk_last_round;
    bool move_to_players;
    bool move_to_point;
    std::atomic<bool> moving;

};