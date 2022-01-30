/*********************************************************************
 * @file   Safe_queue.h
 * @brief  Safe thread implementation of a std::queue<char*>
 *
 * @author Hatz
 * @date   December 2021
 *********************************************************************/

#pragma once

#include <mutex>
#include <queue>
#include <string>

namespace Phoenix
{
    /**
     * @brief Thread safe char* queue
     */
    class Safe_queue
    {
    public:
        void push(const std::string& message);

        void pop();

        std::string front();

        bool empty();

    private:
        std::mutex mutex;
        std::queue<char*> queue;
    };
}


