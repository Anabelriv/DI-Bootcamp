const knex = require('knex');

const db = knex({
    client: 'pg',
    connection: {
        host: 'lucky.db.elephantsql.com',
        port: 5432,
        user: 'kncwsunc',
        password: 'sdkTBD7O5KEzKlL144UKopU_8dz1Ri8i',
        database: 'kncwsunc'
    }
});

const register = async () => {
    const trx = await db.transaction();
    try {
        const user = await db('users')
            .insert({ username: 'bbb', email: 'bbb@gmail.com' }, ['username', 'email']
            )
            .transacting(trx);
        console.log('user =>', user);
        const hashpwd = await db('hashpwd')
            .insert({ username: user[0].username, password: '123456' }, ['password', 'username'])
            .transacting(trx);

        console.log("hashpwd=>", hashpwd);
        // await trx.commit();
        await trx.rollback();
    } catch (err) {
        trx.rollback()
    }
};
register();





// db.select('id', 'name', 'price').from('products').then(rows => {
//     console.log(rows);
// }).catch(err => {
//     console.log(err);
// })

// db('products')
//     .select('id', 'name', 'price')
//     .where({ id: 1 })
//     .then(rows => {
//         console.log(rows[0].name);
//     }).catch(err => {
//         console.log(err);
//     })

// db('products')
//     .insert([
//         { name: 'iChair', price: 400 }
//     ], ["id", "name"])
//     // .returning('*')
//     .then(rows => {
//         console.log(rows);
//     }).catch(err => {
//         console.log(err);
//     });

// db('products')
//     .where({ id: 1 })
//     .update({ name: "iPhone14" }, ["name"])
//     .then(rows => {
//         console.log(rows);
//     }).catch(err => {
//         console.log(err);
//     });

// db('products')
//     .select('id', 'name', 'price')
//     .orderBy('name')
//     .then(rows => {
//         console.log(rows);
//     }).catch(err => {
//         console.log(err);
//     });

// db.raw('select id, name, price from products where id > ?', [1])
//     .then(rows => {
//         console.log(rows.rows);
//     }).catch(err => {
//         console.log(err);
//     });

