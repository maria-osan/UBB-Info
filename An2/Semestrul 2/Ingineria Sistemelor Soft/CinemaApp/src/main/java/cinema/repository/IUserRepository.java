package cinema.repository;

import cinema.domain.User;

public interface IUserRepository extends IRepository<Long, User> {
    User findOne(String username);
}
