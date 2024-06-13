package cinema.domain;

import java.util.Objects;

public class Seat extends Entity<Long> {
    private String nr;
    private int seatRow;
    private int seatColumn;
    private float price;
    private boolean isAvailable;

    public Seat(String nr, int seatRow, int seatColumn, float price, boolean isAvailable) {
        this.nr = nr;
        this.seatRow = seatRow;
        this.seatColumn = seatColumn;
        this.price = price;
        this.isAvailable = isAvailable;
    }

    public String getNr() {
        return nr;
    }

    public void setNr(String nr) {
        this.nr = nr;
    }

    public int getSeatRow() {
        return seatRow;
    }

    public void setSeatRow(int seatRow) {
        this.seatRow = seatRow;
    }

    public int getSeatColumn() {
        return seatColumn;
    }

    public void setSeatColumn(int seatColumn) {
        this.seatColumn = seatColumn;
    }

    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    public boolean isAvailable() {
        return isAvailable;
    }

    public void setAvailable(boolean available) {
        isAvailable = available;
    }

    @Override
    public String toString() {
        return "Seat{" +
                "nr='" + nr + '\'' +
                ", seatRow=" + seatRow +
                ", seatColumn=" + seatColumn +
                ", price=" + price +
                ", isAvailable=" + isAvailable +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Seat seat = (Seat) o;
        return seatRow == seat.seatRow && seatColumn == seat.seatColumn && Float.compare(price, seat.price) == 0 && isAvailable == seat.isAvailable && Objects.equals(nr, seat.nr);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), nr, seatRow, seatColumn, price, isAvailable);
    }
}
