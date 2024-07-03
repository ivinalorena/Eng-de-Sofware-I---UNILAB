type Props = {
  image: string;
  name: string;
};

export default function FoodCategory({ image, name }: Props) {
  return (
    <div className="flex flex-col items-center">
      <img src={image} alt={name} className="w-24 h-24 rounded-full" />
      <span className="mt-2 text-lg">{name}</span>
    </div>
  );
}
