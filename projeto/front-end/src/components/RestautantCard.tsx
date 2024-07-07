type Props = {
  image: string;
  name: string;
  rating: number;
  distance: number;
};

export default function RestaurantCard({ image, name, rating, distance }: Props) {
  return (
    <div className="flex flex-col">
      <img src={image} alt="Restaurant" className="w-full h-32 object-cover rounded mb-4"/>
        <h4 className="text-lg font-bold">{name}</h4>
        <p className="text-gray-600">{rating} • {distance} min</p>
    </div>
  );
}
