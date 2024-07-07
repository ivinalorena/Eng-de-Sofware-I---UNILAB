import { Link } from "react-router-dom";

export default function LoginPage() {
  return (
    <div className="flex min-h-screen">
      <div className="w-1/2 bg-cover bg-center" style={{ backgroundImage: 'url(https://cdn.pixabay.com/photo/2017/07/30/10/33/food-truck-2553919_1280.jpg)' }}>
        <Link to="/">
          <button className="m-4 p-2 bg-gray-800 text-white rounded">Back</button>
        </Link>
      </div>


      <div className="w-1/2 flex flex-col justify-center items-center bg-white">
        <h2 className="text-3xl font-bold mb-8">Faça o seu Login</h2>
        <form className="w-72">
          <div className="mb-4">
            <input type="email" placeholder="Email Address" className="w-full p-2 border rounded" />
          </div>
          <div className="mb-4">
            <input type="password" placeholder="Password" className="w-full p-2 border rounded" />
          </div>
          <button className="w-full p-2 bg-red-500 text-white rounded">Entrar</button>
        </form>
        <Link to="" className="mt-4">
          Ainda não possui conta? <a href="#" className="text-blue-500">registre-se</a>
        </Link>
      </div>
    </div>
  );
}

