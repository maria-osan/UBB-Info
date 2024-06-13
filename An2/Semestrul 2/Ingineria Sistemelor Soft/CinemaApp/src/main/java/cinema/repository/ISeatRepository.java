package cinema.repository;

import cinema.domain.Seat;

public interface ISeatRepository extends IRepository<Long, Seat> {
    Seat findOne(String nr);
}
