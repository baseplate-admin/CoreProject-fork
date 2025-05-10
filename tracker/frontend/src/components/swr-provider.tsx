"use client";

import { ReactNode } from "react";
import { SWRConfig } from "swr";

const map = new Map();

export function SWRProvider({ children }: { children: ReactNode }) {
  return (
    <SWRConfig
      value={{
        provider: () => map,
        refreshInterval: 18000,
      }}
    >
      {children}
    </SWRConfig>
  );
}
