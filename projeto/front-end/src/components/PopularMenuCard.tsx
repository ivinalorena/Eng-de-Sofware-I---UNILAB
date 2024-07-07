import { Link } from "react-router-dom";

type Props = {
  imgSrc: string;
  name: string;
  description: string;
  price: string;
  restaurant: string;
  rating: number;
};

export default function PopularMenuCard({ name, description, imgSrc, price, restaurant, rating }: Props) {
  return (
    <div className="bg-white shadow-md rounded-lg overflow-hidden">
   <div className="bg-white p-4 shadow-md rounded-lg flex flex-col items-center">
        <img src={imgSrc} alt={name} className="w-full h-32 object-cover rounded mb-4" />
        <h4 className="text-lg font-bold">{name}</h4>
        <p className="text-gray-600 mb-2">{description}</p>
        <p className="text-gray-600 mb-2">Feito por: {restaurant}</p>
        <div className="flex justify-between items-center w-full mt-2">
          <span className="text-lg font-bold">${price}</span>
          <span className="text-yellow-500 flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" stroke="currentColor" className="w-6 h-6">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 15l7-7 7 7" />
            </svg>
            {rating}
          </span>
          <Link to="/details">
            <button className="p-2 bg-red-500 text-white rounded">Order</button>
          </Link>
        </div>
      </div>
    </div>
  );
}
