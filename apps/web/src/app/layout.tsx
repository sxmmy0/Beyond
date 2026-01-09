import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/sonner";
import { ApolloProvider } from "@/lib/api/ApolloProvider";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Beyond | Train Smarter. Reach Your Peak.",
  description: "A performance-driven athlete development platform",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <body className={`${inter.className} bg-slate-950 text-white antialiased`}>
        <ApolloProvider>
          {children}
        </ApolloProvider>
        <Toaster />
      </body>
    </html>
  );
}