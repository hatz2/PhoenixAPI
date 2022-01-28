#pragma once

#include "Module.h"
#include "Player.h"
#include "Scene.h"
#include "PhoenixApi/Api.h"
#include <semaphore>
#include <thread>
#include <atomic>
#include <utility>

class Bot : public Module
{
public:
    explicit Bot(Phoenix::Api* api, Player* player, Scene* scene);
    ~Bot();

    void on_send(const std::vector<std::string>& packet_splitted, const std::string& full_packet) override;
    void on_recv(const std::vector<std::string>& packet_splitted, const std::string& full_packet) override;

private:
    void handle_in(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void handle_at(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void handle_su(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void handle_dlgi(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void handle_git(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void handle_npc_req(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void handle_sayi(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void work();

    void complete_room();
    void pick_up_items();
    void attack_garg();
    void walk(int x, int y);

    static constexpr int garg_vnum = 271;
    static constexpr int lever_vnum = 1051;
    static constexpr int crystal_vnum = 1048;
    static constexpr int sunny_meadows_id = 4;
    static constexpr int first_ts_room_id = 4204;
    static constexpr std::pair<int, int> left_portal = { 1, 15 };
    static constexpr std::pair<int, int> right_portal = { 28, 15 };
    static constexpr std::pair<int, int> top_portal = { 14, 1 };
    static constexpr std::pair<int, int> bottom_portal = { 14, 28 };

    std::binary_semaphore map_change;
    std::binary_semaphore garg_spawn;
    std::binary_semaphore lever_pick;
    std::binary_semaphore last_lever_spawn;
    std::thread worker;
    Phoenix::Api* api;
    Player* player;
    Scene* scene;
    std::atomic<int> target_id;
    std::atomic<int> lever_id;
    bool run;
};

