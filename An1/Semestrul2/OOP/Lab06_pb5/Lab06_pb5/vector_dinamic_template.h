#pragma once

#include <assert.h>

#define INITIAL_CAPACITY 10

template <typename element_t>
class iterator_vector_t;


template <typename element_t>
class vector_dinamic_t
{
public:
	// default constructor
	// alocate space for 10 elements
	vector_dinamic_t();

	// copy constructor
	vector_dinamic_t(const vector_dinamic_t& ot); // rule of 3

	// free the memory
	~vector_dinamic_t(); // rule of 3

	// operator assignment
	// free what was in the current object (this)
	// alocate space for elements
	// copy the elements from ot to this
	vector_dinamic_t& operator=(const vector_dinamic_t& ot); // rule of 3

	// move constructor
	// called if we build a new vector from an r-value (ex temporary, expression from return)
	// the ot object is no longer used, so its interior can be reused
	vector_dinamic_t(vector_dinamic_t&& ot); // rule of 5

	// move assignment
	// similar to move constructor
	// used for assignment
	vector_dinamic_t& operator=(vector_dinamic_t&& ot); // rule of 5

	void add(const element_t& el);

	void del(int poz, const element_t el);

	element_t& get_elem(int poz) const;

	void set(int poz, const element_t& el);

	int size() const noexcept;

	friend class iterator_vector_t<element_t>;

	// functions that create the iterators
	iterator_vector_t<element_t> begin();
	iterator_vector_t<element_t> end();

private:
	int lg; // number of elements
	int cap; // capacity
	element_t* elems; // the elements

	void ensure_capacity();
};


template <typename element_t>
void vector_dinamic_t<element_t>::ensure_capacity()
{
	if (lg < cap)
		return; // we still have space

	cap *= 2;
	element_t* aux = new element_t[cap];
	for (int i = 0; i < lg; i++)
		aux[i] = elems[i];
	delete[] elems;
	elems = aux;
}

// default constructor
// alocate space for 10 elements
template <typename element_t>
vector_dinamic_t<element_t>::vector_dinamic_t() :elems{ new element_t[INITIAL_CAPACITY] }, cap{ INITIAL_CAPACITY }, lg{ 0 } {}

// copy constructor
// the current object (this) is now being created
// alocate space for elements
// copy the elements from ot to this
template <typename element_t>
vector_dinamic_t<element_t>::vector_dinamic_t(const vector_dinamic_t<element_t>& ot)
{
	elems = new element_t[ot.cap];
	// copy the elements
	for (int i = 0; i < ot.lg; i++)
		elems[i] = ot.elems[i]; // assignment from Disciplina
	lg = ot.lg;
	cap = ot.cap;
}

// free the memory
template <typename element_t>
vector_dinamic_t<element_t>::~vector_dinamic_t()
{
	delete[] elems;
}

// operator assignment
// free what was in the current object (this)
// alocate space for elements
// copy the elements from ot to this
template <typename element_t>
vector_dinamic_t<element_t>& vector_dinamic_t<element_t>::operator=(const vector_dinamic_t& ot)
{
	if (this == &ot)
		return *this;

	delete[] elems;
	elems = new element_t[ot.cap];
	// copy the elements
	for (int i = 0; i < ot.lg; i++)
		elems[i] = ot.elems[i]; // assignment from Disciplina
	lg = ot.lg;
	cap = ot.cap;
	return *this;
}

// move constructor
// called if we build a new vector from an r-value (ex temporary, expression from return)
// the ot object is no longer used, so its interior can be reused
template <typename element_t>
vector_dinamic_t<element_t>::vector_dinamic_t(vector_dinamic_t&& ot)
{
	// copy the data pointer from other
	elems = ot.elems;
	lg = ot.lg;
	cap = ot.cap;

	// relase the data pointer from the source object so that
	// the destructor does not free the memory multiple times
	ot.elems = nullptr;
	ot.lg = 0;
	ot.cap = 0;
}

// move assignment
// similar to move constructor
// used for assignment
// releases the contents of the current object (this)
// "steal" the inside of ot
// prepare ot for destruction
template <typename element_t>
vector_dinamic_t<element_t>& vector_dinamic_t<element_t>::operator=(vector_dinamic_t&& ot)
{
	if (this == &ot)
		return *this;

	delete[] elems;
	// copy the data pointer from other
	elems = ot.elems;
	lg = ot.lg;
	cap = ot.cap;

	// relase the data pointer from the source object so that
	// the destructor does not free the memory multiple times
	ot.elems = nullptr;
	ot.lg = 0;
	ot.cap = 0;
	return *this;
}

template <typename element_t>
void vector_dinamic_t<element_t>::add(const element_t& el)
{
	ensure_capacity(); // if it's necessary we allocate more memory
	elems[lg++] = el;
}

template <typename element_t>
void vector_dinamic_t<element_t>::del(int poz, const element_t el)
{
	element_t* aux = new element_t[lg];
	for (int i = 0; i < poz; i++)
		aux[i] = elems[i];
	for (int i = poz+1; i < lg; i++)
		aux[i-1] = elems[i];
	delete[] elems;
	elems = aux;
	lg--;
}

template <typename element_t>
element_t& vector_dinamic_t<element_t>::get_elem(int poz) const
{
	return elems[poz];
}

template <typename element_t>
void vector_dinamic_t<element_t>::set(int poz, const element_t& el)
{
	elems[poz] = el;
}

template <typename element_t>
int vector_dinamic_t<element_t>::size() const noexcept
{
	return lg;
}

template <typename element_t>
iterator_vector_t<element_t> vector_dinamic_t<element_t>::begin()
{
	return iterator_vector_t<element_t>(*this);
}

template <typename element_t>
iterator_vector_t<element_t> vector_dinamic_t<element_t>::end()
{
	return iterator_vector_t<element_t>(*this, lg);
}


template <typename element_t>
class iterator_vector_t
{
private:
	const vector_dinamic_t<element_t>& v;
	int poz = 0;

public:
	iterator_vector_t(const vector_dinamic_t<element_t>& v) noexcept;
	iterator_vector_t(const vector_dinamic_t<element_t>& v, int poz) noexcept;

	bool valid() const noexcept;
	element_t& elem() const noexcept;
	void next() noexcept;

	element_t& operator*();
	iterator_vector_t& operator++();
	bool operator==(const iterator_vector_t& ot) noexcept;
	bool operator!=(const iterator_vector_t& ot) noexcept;
};


template <typename element_t>
iterator_vector_t<element_t>::iterator_vector_t(const vector_dinamic_t<element_t>& v) noexcept :v{ v } {}

template <typename element_t>
iterator_vector_t<element_t>::iterator_vector_t(const vector_dinamic_t<element_t>& v, int poz) noexcept :v{ v }, poz{ poz } {}

template <typename element_t>
bool iterator_vector_t<element_t>::valid() const noexcept
{
	return poz < v.lg;
}

template <typename element_t>
element_t& iterator_vector_t<element_t>::elem() const noexcept
{
	return v.elems[poz];
}

template <typename element_t>
void iterator_vector_t<element_t>::next() noexcept
{
	poz++;
}

template <typename element_t>
element_t& iterator_vector_t<element_t>::operator*()
{
	return elem();
}

template <typename element_t>
iterator_vector_t<element_t>& iterator_vector_t<element_t>::operator++()
{
	next();
	return *this;
}

template <typename element_t>
bool iterator_vector_t<element_t>::operator==(const iterator_vector_t<element_t>& ot) noexcept
{
	return poz == ot.poz;
}

template <typename element_t>
bool iterator_vector_t<element_t>::operator!=(const iterator_vector_t<element_t>& ot) noexcept
{
	return !(*this == ot);
}


// ---TESTS---
template <typename my_vector>
void test_create_copy_assign_t()
{
	// Test for constructors / assignments
	my_vector v; // default constructor
	Disciplina d = { "5006", "POO", "1", "seminar", "Czibula Istvan" };
	v.add(d);
	assert(v.size() == 1);
	assert(v.get_elem(0).get_type() == "seminar");

	for (int i = 1; i < 15; i++)
		v.add(d);
	assert(v.size() == 15);
	assert(v.get_elem(11).get_name() == "POO");

	my_vector v2{ v }; // copy constructor
	assert(v2.size() == 15);
	assert(v2.get_elem(11).get_name() == "POO");

	my_vector v3; // default constructor
	v3 = v; // operator= assignment
	assert(v3.size() == 15);
	assert(v3.get_elem(11).get_name() == "POO");
}

template <typename my_vector>
void test_vector_dinamic_template()
{
	test_create_copy_assign_t<my_vector>();
}