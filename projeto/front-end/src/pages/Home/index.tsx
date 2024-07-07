import React from 'react';
import { DataCart, PopularMenuItems } from '../../Mock/data';
import PopularMenuCard from '../../components/PopularMenuCard';
import RestaurantCard from '../../components/RestautantCard';

const Home: React.FC = () => {
  return (
    <div className="min-h-screen px-8">
      <main className="mt-8">
        <section className="text-center mb-8">
          <h2 className="text-4xl font-bold mb-4">Encontre Sua Comida Favorita</h2>
          <p className="text-gray-600 mb-4">O que você quer pedir?</p>
          <div className="flex justify-center mb-4">
            <input type="text" placeholder="Pesquisar..." className="p-2 border rounded-l" />
            <button className="p-2 bg-red-500 text-white rounded-r">Pesquisar</button>
          </div>
          <div className="flex justify-center space-x-4">
            <button className="p-2 bg-gray-200 rounded">Todos</button>
            <button className="p-2 bg-gray-200 rounded">Pizza</button>
            <button className="p-2 bg-gray-200 rounded">Bebidas</button>
            <button className="p-2 bg-gray-200 rounded">Asiática</button>
            <button className="p-2 bg-gray-200 rounded">Sobremesas</button>
            <button className="p-2 bg-gray-200 rounded">Hambúrgueres</button>
          </div>
        </section>

        <section className="mb-8">
          <h3 className="text-2xl font-bold mb-4">Restaurantes Mais Próximos</h3>
          <div className="grid grid-cols-4 gap-4">
            {DataCart.map((restaurant) => (
              <RestaurantCard
                distance={restaurant.distance}
                image={restaurant.image}
                name={restaurant.name}
                rating={restaurant.rating}
                key={restaurant.name}
              />
            ))}
          </div>
        </section>

        <section className="mb-8">
          <h3 className="text-2xl font-bold mb-4">Menu Popular</h3>
          <div className="grid grid-cols-4 gap-4">
            {PopularMenuItems.map((item, index) => (
              <PopularMenuCard
                key={index}
                imgSrc={item.imgSrc}
                name={item.name}
                description={item.description}
                price={item.price}
                restaurant={item.restaurant}
                rating={item.rating}
              />
            ))}
          </div>
        </section>
      </main>
    </div>
  );
};

export default Home;
