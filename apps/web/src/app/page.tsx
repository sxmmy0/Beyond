import Link from "next/link";
import { Flame, ArrowRight } from "lucide-react";
import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 flex items-center justify-center">
      {/* Background effects */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute top-1/4 -left-20 w-96 h-96 bg-emerald-500/10 rounded-full blur-3xl" />
        <div className="absolute bottom-1/4 -right-20 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl" />
      </div>

      <div className="relative z-10 text-center px-4">
        {/* Logo */}
        <div className="mx-auto mb-8 flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-emerald-400 to-cyan-400">
          <Flame className="h-9 w-9 text-slate-900" />
        </div>

        {/* Hero Text */}
        <h1 className="text-5xl md:text-6xl font-bold text-white mb-4">
          Train Smarter.
          <br />
          <span className="bg-gradient-to-r from-emerald-400 to-cyan-400 bg-clip-text text-transparent">
            Reach Your Peak.
          </span>
        </h1>
        <p className="text-xl text-slate-400 max-w-xl mx-auto mb-8">
          AI-powered athlete development platform that blends personalized coaching, 
          smart training guidance, and community support.
        </p>

        {/* CTA Buttons */}
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <Button
            asChild
            size="lg"
            className="bg-gradient-to-r from-emerald-500 to-cyan-500 text-slate-900 font-semibold hover:from-emerald-400 hover:to-cyan-400"
          >
            <Link href="/register">
              Get Started
              <ArrowRight className="ml-2 h-4 w-4" />
            </Link>
          </Button>
          <Button
            asChild
            size="lg"
            variant="outline"
            className="border-slate-700 text-white hover:bg-slate-800"
          >
            <Link href="/login">Sign In</Link>
          </Button>
        </div>
      </div>
    </div>
  );
}