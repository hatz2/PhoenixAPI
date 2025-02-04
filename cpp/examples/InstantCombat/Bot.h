#pragma once
#include "Module.h"
#include "Scene.h"
#include "PhoenixApi/Api.h"
#include "INIReader.h"
#include "Logger.h"
#include <utility>
#include <thread>
#include <ctime>
#include <random>

class Bot : public Module
{
public:
    explicit Bot(Phoenix::Api* api, Scene* scene);

    void on_recv(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void run();
    void handle_map_entities(const nlohmann::json& data);

private:
    void handle_qnamli(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void handle_msgi(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void handle_cmap(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void handle_in(const std::vector<std::string>& packet_splitted, const std::string& full_packet);

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
    bool moving;
    bool waiting_for_spawn;
    int current_map_id;
    clock_t time_begin;
    std::mt19937 generator;
};