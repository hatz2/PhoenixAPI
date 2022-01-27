#pragma once

#include "Module.h"
#include <map>
#include <set>

class Scene : public Module
{
public:
    void on_recv(const std::vector<std::string>& packet_splitted);

    size_t get_monster_count() const;
    size_t get_items_count() const;
    size_t get_levers_count() const;

    const std::set<int> get_items() const;

private:
    void handle_in(const std::vector<std::string>& packet_splitted);
    void handle_out(const std::vector<std::string>& packet_splitted);
    void handle_su(const std::vector<std::string>& packet_splitted);
    void handle_drop(const std::vector<std::string>& packet_splitted);
    void handle_get(const std::vector<std::string>& packet_splitted);
    void handle_cmap(const std::vector<std::string>& packet_splitted);

    std::map<int /* id */, int /* vnum */> monsters;
    std::set<int /* id */> items;
    std::set<int /* id */> levers;
};

