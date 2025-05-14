import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Health Check",
  description: "This route is used to check the health of the tracker.",
};

export default function HealthLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return <>{children}</>;
}
