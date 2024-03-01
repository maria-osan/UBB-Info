package com.example.lab10_2.repository;

import com.example.lab10_2.domain.User;
import com.example.lab10_2.dto.UserFilterDTO;

public interface UserRepository extends PagingRepository<Long, User>{
    Page<User> findAll(Pageable pageable, UserFilterDTO filter);
}
