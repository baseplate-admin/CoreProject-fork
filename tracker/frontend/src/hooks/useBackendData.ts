"use client";
import useSWR from "swr";
import { API_URL } from "@/constants/url";
import { BackendData } from "@/types/api";

export const URL = API_URL;

const fetcher = async (url: URL) => {
  const res = await fetch(url);

  const data = await res.json();

  return data;
};

export function useBackendData() {
  const { data, error, isLoading } = useSWR<BackendData>(API_URL, fetcher);

  return {
    data: data ?? null,
    isLoading,
    isError: error,
  };
}
