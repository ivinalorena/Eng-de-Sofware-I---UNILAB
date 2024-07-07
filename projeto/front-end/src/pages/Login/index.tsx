import { Link } from "react-router-dom";
import { useForm } from "react-hook-form";
import { zodResolver } from '@hookform/resolvers/zod';
import * as z from 'zod';

const loginFormSchema = z.object({
  email: z.string().email("Email inválido"),
  password: z.string().min(6, "A senha deve ter pelo menos 6 caracteres")
});

type LoginFormInputs = z.infer<typeof loginFormSchema>;

export default function LoginPage() {
  const { register, handleSubmit, reset, formState: { errors, isSubmitting } } = useForm<LoginFormInputs>({
    resolver: zodResolver(loginFormSchema),
    defaultValues: {
      email: '',
      password: ''
    }
  });

  async function handleLogin(data: LoginFormInputs) {
    console.log(data);
    reset();
  }

  return (
    <div className="flex min-h-screen">
      <div className="w-1/2 bg-cover bg-center" style={{ backgroundImage: 'url(https://cdn.pixabay.com/photo/2017/07/30/10/33/food-truck-2553919_1280.jpg)' }}>
        <Link to="/">
          <button className="m-4 p-2 bg-gray-800 text-white rounded">Back</button>
        </Link>
      </div>
      <div className="w-1/2 flex flex-col justify-center items-center bg-white">
        <h2 className="text-3xl font-bold mb-8">Faça o seu Login</h2>
        <form className="w-72" onSubmit={handleSubmit(handleLogin)}>
          <div className="mb-4">
            <input 
              type="email" 
              placeholder="Email Address" 
              className="w-full p-2 border rounded"
              {...register('email')}
            />
            {errors.email && <p className="text-red-500 text-xs mt-1">{errors.email.message}</p>}
          </div>
          <div className="mb-4">
            <input 
              type="password" 
              placeholder="Password" 
              className="w-full p-2 border rounded"
              {...register('password')}
            />
            {errors.password && <p className="text-red-500 text-xs mt-1">{errors.password.message}</p>}
          </div>
          <button
            type="submit"
            className="w-full p-2 bg-red-500 text-white rounded"
            disabled={isSubmitting}
          >Entrar</button>
        </form>
        <div className="mt-4">
          Ainda não possui conta? <Link to="/register" className="text-blue-500">Registre-se</Link>
        </div>
      </div>
    </div>
  );
}
