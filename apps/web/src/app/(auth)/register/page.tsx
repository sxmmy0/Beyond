"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import { Eye, EyeOff, Flame, Loader2 } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { toast } from "sonner";

const registerSchema = z.object({
  username: z.string().min(3, "Username must be at least 3 characters"),
  email: z.string().email("Please enter a valid email"),
  password: z.string().min(8, "Password must be at least 8 characters"),
  confirmPassword: z.string(),
}).refine((data) => data.password === data.confirmPassword, {
  message: "Passwords don't match",
  path: ["confirmPassword"],
});

type RegisterFormData = z.infer<typeof registerSchema>;

const GRAPHQL_URL = process.env.NEXT_PUBLIC_GRAPHQL_URL || "http://localhost:8000/graphql/";

export default function RegisterPage() {
  const router = useRouter();
  const [showPassword, setShowPassword] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<RegisterFormData>({
    resolver: zodResolver(registerSchema),
  });

  const onSubmit = async (data: RegisterFormData) => {
    setIsLoading(true);
    
    try {
      const response = await fetch(GRAPHQL_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include",
        body: JSON.stringify({
          query: `
            mutation Register($input: RegisterInput!) {
              register(input: $input) {
                id
                email
                username
                role
              }
            }
          `,
          variables: {
            input: {
              email: data.email,
              username: data.username,
              password: data.password,
            },
          },
        }),
      });

      const result = await response.json();

      if (result.errors) {
        throw new Error(result.errors[0].message);
      }

      toast.success("Account created!", {
        description: `Welcome to Beyond, ${result.data.register.username}!`,
      });
      router.push("/dashboard");
    } catch (error) {
      toast.error("Registration failed", {
        description: error instanceof Error ? error.message : "An error occurred",
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Card className="border-slate-800 bg-slate-900/50 backdrop-blur-sm">
      <CardHeader className="text-center">
        <div className="mx-auto mb-4 flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-br from-emerald-400 to-cyan-400">
          <Flame className="h-7 w-7 text-slate-900" />
        </div>
        <CardTitle className="text-2xl text-white">Create your account</CardTitle>
        <CardDescription className="text-slate-400">
          Start your journey to peak performance
        </CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <div className="space-y-2">
            <Label htmlFor="username" className="text-slate-300">
              Username
            </Label>
            <Input
              id="username"
              type="text"
              placeholder="johndoe"
              {...register("username")}
              className="border-slate-700 bg-slate-800 text-white placeholder:text-slate-500 focus-visible:ring-emerald-500"
            />
            {errors.username && (
              <p className="text-sm text-red-400">{errors.username.message}</p>
            )}
          </div>
          <div className="space-y-2">
            <Label htmlFor="email" className="text-slate-300">
              Email
            </Label>
            <Input
              id="email"
              type="email"
              placeholder="athlete@example.com"
              {...register("email")}
              className="border-slate-700 bg-slate-800 text-white placeholder:text-slate-500 focus-visible:ring-emerald-500"
            />
            {errors.email && (
              <p className="text-sm text-red-400">{errors.email.message}</p>
            )}
          </div>
          <div className="space-y-2">
            <Label htmlFor="password" className="text-slate-300">
              Password
            </Label>
            <div className="relative">
              <Input
                id="password"
                type={showPassword ? "text" : "password"}
                placeholder="••••••••"
                {...register("password")}
                className="border-slate-700 bg-slate-800 pr-10 text-white placeholder:text-slate-500 focus-visible:ring-emerald-500"
              />
              <button
                type="button"
                onClick={() => setShowPassword(!showPassword)}
                className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-500 hover:text-slate-300"
              >
                {showPassword ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
              </button>
            </div>
            {errors.password && (
              <p className="text-sm text-red-400">{errors.password.message}</p>
            )}
          </div>
          <div className="space-y-2">
            <Label htmlFor="confirmPassword" className="text-slate-300">
              Confirm Password
            </Label>
            <Input
              id="confirmPassword"
              type="password"
              placeholder="••••••••"
              {...register("confirmPassword")}
              className="border-slate-700 bg-slate-800 text-white placeholder:text-slate-500 focus-visible:ring-emerald-500"
            />
            {errors.confirmPassword && (
              <p className="text-sm text-red-400">{errors.confirmPassword.message}</p>
            )}
          </div>
          <Button
            type="submit"
            disabled={isLoading}
            className="w-full bg-gradient-to-r from-emerald-500 to-cyan-500 text-slate-900 font-semibold hover:from-emerald-400 hover:to-cyan-400"
          >
            {isLoading ? (
              <>
                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                Creating account...
              </>
            ) : (
              "Create account"
            )}
          </Button>
        </form>
      </CardContent>
      <CardFooter className="justify-center">
        <p className="text-sm text-slate-400">
          Already have an account?{" "}
          <Link href="/login" className="text-emerald-400 hover:text-emerald-300">
            Sign in
          </Link>
        </p>
      </CardFooter>
    </Card>
  );
}
