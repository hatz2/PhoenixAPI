/*********************************************************************
 * @file   Port_finder.h
 * @brief  Additional API function to get the ports
 *
 * @author Hatz
 * @date   December 2021
 *********************************************************************/

#pragma once

#include <vector>

namespace Phoenix
{
    /**
     * @brief Find the ports from all the running bots
     * @return std::vector with the ports
     */
    std::vector<int> find_ports();
}

