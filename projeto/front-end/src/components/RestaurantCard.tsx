type Props = {
  image: string;
  name: string;
  description: string;
};

export default function RestaurantCard({ image, name, description }: Props) {
  return (
    <div className="bg-white shadow-md rounded-lg overflow-hidden">
      <img src={image} alt={name} className="w-full h-32 sm:h-48 object-cover" />
      <div className="p-4">
        <h3 className="text-lg font-bold">{name}</h3>
        <p className="text-gray-600">{description}</p>
      </div>
    </div>
  );
}
