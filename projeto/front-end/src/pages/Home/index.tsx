import FoodCategory from "../../components/FoodCategory";
import RestaurantCard from "../../components/RestaurantCard";

const foodCategories = [
  { image: 'https://cdn.pixabay.com/photo/2020/06/08/16/49/pizza-5275191_960_720.jpg', name: 'Pizza' },
  { image: 'https://cdn.pixabay.com/photo/2017/10/15/11/41/sushi-2853382_1280.jpg', name: 'Sushi' },
  // Adicione mais categorias conforme necessário
];

const restaurants = [
  { image: 'https://cdn.pixabay.com/photo/2020/06/08/16/49/pizza-5275191_960_720.jpg', name: 'Pizza Palace', description: 'Delicious wood-fired pizza.' },
  { image: 'https://cdn.pixabay.com/photo/2017/10/15/11/41/sushi-2853382_1280.jpg', name: 'Sushi World', description: 'Fresh sushi and sashimi.' },
  // Adicione mais restaurantes conforme necessário
];

export default function Home() {
  return (
    <div>
      <main className="p-4">
        <section className="my-8">
          <h2 className="text-2xl font-bold mb-4">Categorias de Comida</h2>
          <div className="flex space-x-4 overflow-x-auto">
            {foodCategories.map((category, index) => (
              <FoodCategory key={index} image={category.image} name={category.name} />
            ))}
          </div>
        </section>
        <section className="my-8">
          <h2 className="text-2xl font-bold mb-4">Restaurantes Populares</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {restaurants.map((restaurant, index) => (
              <RestaurantCard key={index} image={restaurant.image} name={restaurant.name} description={restaurant.description} />
            ))}
          </div>
        </section>
        <section className="my-8 text-center">
          <h2 className="text-2xl font-bold mb-4">Baixe o App</h2>
          <p className="mb-4">Peça sua comida favorita a qualquer hora, em qualquer lugar.</p>
          <button className="bg-red-500 text-yellow-400 py-2 px-4 rounded-lg">Baixar Agora</button>
        </section>
      </main>
    </div>
  );
}
