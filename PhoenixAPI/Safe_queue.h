#pragma once

#include <mutex>
#include <queue>
#include <string>

namespace Phoenix
{
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


