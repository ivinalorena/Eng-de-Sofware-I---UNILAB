import React from 'react';
import { Link } from "react-router-dom";
import { useForm } from "react-hook-form";
import { zodResolver } from '@hookform/resolvers/zod';
import * as z from 'zod';

// Definir o esquema do formulário usando Zod
const registerFormSchema = z.object({
  email: z.string().email("Email inválido"),
  password: z.string().min(6, "A senha deve ter pelo menos 6 caracteres"),
  confirmPassword: z.string().min(6, "A confirmação de senha deve ter pelo menos 6 caracteres")
}).refine(data => data.password === data.confirmPassword, {
  message: "As senhas não coincidem",
  path: ["confirmPassword"]
});

type RegisterFormInputs = z.infer<typeof registerFormSchema>;

export default function Register() {
  const { register, handleSubmit, reset, formState: { errors, isSubmitting } } = useForm<RegisterFormInputs>({
    resolver: zodResolver(registerFormSchema),
    defaultValues: {
      email: '',
      password: '',
      confirmPassword: ''
    }
  });

  async function handleRegisterUser(data: RegisterFormInputs) {
    console.log(data);
    reset();
  }

  return (
    <div className="flex min-h-screen">
      <div className="w-1/2 bg-cover bg-center" style={{ backgroundImage: 'url(https://cdn.pixabay.com/photo/2017/07/30/10/33/food-truck-2553919_1280.jpg)' }}>
        <Link to="/">
          <button className="m-4 p-2 bg-gray-800 text-white rounded">Voltar</button>
        </Link>
      </div>
      <div className="w-1/2 flex flex-col justify-center items-center bg-white">
        <h2 className="text-3xl font-bold mb-8">Crie sua Conta</h2>
        <form className="w-72" onSubmit={handleSubmit(handleRegisterUser)}>
          <div className="mb-4">
            <input 
              type="email" 
              placeholder="Endereço de Email" 
              className="w-full p-2 border rounded"
              {...register('email')}
            />
            {errors.email && <p className="text-red-500 text-xs mt-1">{errors.email.message}</p>}
          </div>
          <div className="mb-4">
            <input 
              type="password" 
              placeholder="Senha" 
              className="w-full p-2 border rounded"
              {...register('password')}
            />
            {errors.password && <p className="text-red-500 text-xs mt-1">{errors.password.message}</p>}
          </div>
          <div className="mb-4">
            <input 
              type="password" 
              placeholder="Confirme sua Senha" 
              className="w-full p-2 border rounded"
              {...register('confirmPassword')}
            />
            {errors.confirmPassword && <p className="text-red-500 text-xs mt-1">{errors.confirmPassword.message}</p>}
          </div>
        
          <button
            type="submit"
            className="w-full p-2 bg-red-500 text-white rounded"
            disabled={isSubmitting}
          >Registrar
          </button>
        </form>
        <div className="mt-4">
          Já possui uma conta? <Link to="/login" className="text-blue-500">Faça login</Link>
        </div>
      </div>
    </div>
  );
}
