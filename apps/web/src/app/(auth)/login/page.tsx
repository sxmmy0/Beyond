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

const loginSchema = z.object({
  email: z.string().email("Please enter a valid email"),
  password: z.string().min(8, "Password must be at least 8 characters"),
});

type LoginFormData = z.infer<typeof loginSchema>;

const GRAPHQL_URL = process.env.NEXT_PUBLIC_GRAPHQL_URL || "http://localhost:8000/graphql/";

export default function LoginPage() {
  const router = useRouter();
  const [showPassword, setShowPassword] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginFormData>({
    resolver: zodResolver(loginSchema),
  });

  const onSubmit = async (data: LoginFormData) => {
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
            mutation Login($input: LoginInput!) {
              login(input: $input) {
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
              password: data.password,
            },
          },
        }),
      });

      const result = await response.json();

      if (result.errors) {
        throw new Error(result.errors[0].message);
      }

      toast.success("Welcome back!", {
        description: `Logged in as ${result.data.login.email}`,
      });
      router.push("/dashboard");
    } catch (error) {
      toast.error("Login failed", {
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
        <CardTitle className="text-2xl text-white">Welcome back</CardTitle>
        <CardDescription className="text-slate-400">
          Sign in to continue your training journey
        </CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
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
          <div className="flex justify-end">
            <Link
              href="/forgot-password"
              className="text-sm text-emerald-400 hover:text-emerald-300"
            >
              Forgot password?
            </Link>
          </div>
          <Button
            type="submit"
            disabled={isLoading}
            className="w-full bg-gradient-to-r from-emerald-500 to-cyan-500 text-slate-900 font-semibold hover:from-emerald-400 hover:to-cyan-400"
          >
            {isLoading ? (
              <>
                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                Signing in...
              </>
            ) : (
              "Sign in"
            )}
          </Button>
        </form>
      </CardContent>
      <CardFooter className="justify-center">
        <p className="text-sm text-slate-400">
          Don&apos;t have an account?{" "}
          <Link href="/register" className="text-emerald-400 hover:text-emerald-300">
            Sign up
          </Link>
        </p>
      </CardFooter>
    </Card>
  );
}
