const customer = {
    first_name : 'Peter',
    last_name : 'Parker',
    birth_date : 'August 10, 2001',
    gender: 'male',
    address: {
        street : '20 Ingram Street',
        city : 'Forest Hills',
        state : 'NY',
        zip : '11375',
    },
    email : 'greatpower@greatresponsibility.com',
    phone : '123-456-7890',
    room_preferences: ['double', 'pool view', 'wheelchair accessible'],
    check_in_date : {
        month : 'February',
        day : 17,
        year : 2024,
    },
    check_out_date : {
        month : 'February',
        day : 20,
        year : 2024,
    },
    getAge : function() {
        const today = new Date();
        return today.getFullYear() - this.year;
    },
    durationOfStay : function() {
        const checkIn = new Date(this.check_in_date.year, this.check_in_date.month, this.check_in_date.day);
        const checkOut = new Date(this.check_out_date.year, this.check_out_date.month, this.check_out_date.day);
        return Math.ceil(checkOut - checkIn) / (1000 * 60 * 60 * 24);
    },
}

const customer_information = `
    Customer Information:
    First Name: ${customer.first_name}
    Last Name: ${customer.last_name}
    Birth Date: ${customer.birth_date}
    Gender: ${customer.gender}
    Address: ${customer.address.street}, ${customer.address.city}, ${customer.address.state} ${customer.address.zip}
    Email: ${customer.email}
    Phone: ${customer.phone}
    Room Preferences: ${customer.room_preferences.join(', ')}
    Check In Date: ${customer.check_in_date.month} ${customer.check_in_date.day}, ${customer.check_in_date.year}
    Check Out Date: ${customer.check_out_date.month} ${customer.check_out_date.day}, ${customer.check_out_date.year}
    Age: ${customer.getAge()}
    Duration of Stay: ${customer.durationOfStay()} days
    `
    console.log(customer_information);
