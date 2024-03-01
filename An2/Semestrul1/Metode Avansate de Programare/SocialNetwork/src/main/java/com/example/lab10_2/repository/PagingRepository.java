package com.example.lab10_2.repository;

import com.example.lab10_2.domain.Entity;

public interface PagingRepository<ID, E extends Entity<ID>> extends Repository<ID, E> {
    Page<E> findAll(Pageable pageable);
}
