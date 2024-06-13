package cinema.domain;

import java.util.List;
import java.util.Objects;

public class Ticket extends Entity<Long> {
    private String buyerName;
    private long idMovie;
    private float price;
    private List<Seat> seats;

    public Ticket(String buyerName, long idMovie, float price, List<Seat> seats) {
        this.buyerName = buyerName;
        this.idMovie = idMovie;
        this.price = price;
        this.seats = seats;
    }

    public String getBuyerName() {
        return buyerName;
    }

    public void setBuyerName(String buyerName) {
        this.buyerName = buyerName;
    }

    public long getIdMovie() {
        return idMovie;
    }

    public void setIdMovie(long idMovie) {
        this.idMovie = idMovie;
    }

    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    public List<Seat> getSeats() {
        return seats;
    }

    public void setSeats(List<Seat> seats) {
        this.seats = seats;
    }

    @Override
    public String toString() {
        return "Ticket{" +
                "BuyerName='" + buyerName + '\'' +
                ", idMovie=" + idMovie +
                ", price=" + price +
                ", seats=" + seats +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Ticket ticket = (Ticket) o;
        return idMovie == ticket.idMovie && Float.compare(price, ticket.price) == 0 && Objects.equals(buyerName, ticket.buyerName) && Objects.equals(seats, ticket.seats);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), buyerName, idMovie, price, seats);
    }
}
