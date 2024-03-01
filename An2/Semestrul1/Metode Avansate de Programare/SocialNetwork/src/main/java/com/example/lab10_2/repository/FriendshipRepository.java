package com.example.lab10_2.repository;

import com.example.lab10_2.domain.Friendship;
import com.example.lab10_2.dto.FriendshipFilterDTO;

public interface FriendshipRepository extends PagingRepository<Long, Friendship> {
    Page<Friendship> findAll(Pageable pageable, FriendshipFilterDTO filter);
}
