"use client";

import {
  useState,
  useCallback,
  useMemo,
  useRef,
  forwardRef,
  useEffect,
  useImperativeHandle,
} from "react";
import maplibregl, { Map as MapType, MapMouseEvent } from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";
import { MapLibre } from "@/components/custom/map";
// Country coordinate data
const COUNTRY_COORDINATES: Record<string, [number, number]> = {
  US: [-98.5795, 39.8283], // United States
  DE: [10.4515, 51.1657], // Germany
  CN: [104.1954, 35.8617], // China
  IN: [78.9629, 20.5937], // India
  BR: [-53.2, -10.3333], // Brazil
  NG: [8.6753, 9.082], // Nigeria
};

interface TrafficFlow {
  source: string;
  destination: string;
  value: number;
  x?: number;
  y?: number;
}

export default function NetworkTrafficMap() {
  const [hoveredFlow, setHoveredFlow] = useState<TrafficFlow | null>(null);
  const mapRef = useRef<MapType>(null);

  const trafficFlows = useMemo(() => generateMockTrafficData(), []);

  const trafficData = useMemo(
    () => ({
      type: "FeatureCollection" as const,
      features: trafficFlows.map((flow) => ({
        type: "Feature" as const,
        geometry: {
          type: "LineString" as const,
          coordinates: [
            COUNTRY_COORDINATES[flow.source],
            COUNTRY_COORDINATES[flow.destination],
          ],
        },
        properties: {
          ...flow,
          color: getColorForTraffic(flow.value),
        },
      })),
    }),
    [trafficFlows],
  );

  const onMapLoad = useCallback(
    (map: MapType) => {
      map.addControl(new maplibregl.NavigationControl());

      map.addSource("traffic-flow", {
        type: "geojson",
        data: trafficData,
      });

      map.addLayer({
        id: "traffic-flow",
        type: "line",
        source: "traffic-flow",
        paint: {
          "line-color": ["get", "color"],
          "line-width": [
            "interpolate",
            ["linear"],
            ["get", "value"],
            0,
            1,
            100,
            5,
          ],
          "line-opacity": 0.7,
          "line-dasharray": [0, 2, 2, 2],
        },
      });

      let animationFrame: number;
      const animateLine = () => {
        map.setPaintProperty("traffic-flow", "line-dasharray", {
          stops: [[0, [0, 4, 0, 4]]],
          base: 2,
        });
        animationFrame = requestAnimationFrame(animateLine);
      };
      animateLine();

      return () => cancelAnimationFrame(animationFrame);
    },
    [trafficData],
  );

  const handleMouseMove = useCallback((map: MapType, e: MapMouseEvent) => {
    const features = map.queryRenderedFeatures(e.point, {
      layers: ["traffic-flow"],
    });

    if (features[0]?.properties) {
      const flow = features[0].properties as TrafficFlow;
      setHoveredFlow({
        ...flow,
        x: e.point.x,
        y: e.point.y,
      });

      map.setFilter("country-label", [
        "match",
        ["get", "iso_3166_1"],
        [flow.source, flow.destination],
        true,
        false,
      ]);
    } else {
      setHoveredFlow(null);
      map.setFilter("country-label", ["has", "iso_3166_1"]);
    }
  }, []);

  return (
    <div className="relative h-[600px] w-full">
      <MapLibre
        ref={mapRef}
        className="rounded-xl border shadow-sm"
        initialViewState={{
          longitude: 20,
          latitude: 30,
          zoom: 1.5,
        }}
        onLoad={onMapLoad}
        onMouseMove={handleMouseMove}
        onMouseLeave={() => setHoveredFlow(null)}
      />

      {hoveredFlow && (
        <div
          className="bg-background pointer-events-none absolute rounded-lg border p-3 shadow-lg"
          style={{
            left: hoveredFlow.x! + 10,
            top: hoveredFlow.y! - 10,
          }}
        >
          <div className="text-sm font-medium">
            {hoveredFlow.source} → {hoveredFlow.destination}
          </div>
          <div className="text-muted-foreground text-xs">
            Traffic: {formatTrafficValue(hoveredFlow.value)}
          </div>
        </div>
      )}
    </div>
  );
}

// Helper functions
function generateMockTrafficData(): TrafficFlow[] {
  const countries = Object.keys(COUNTRY_COORDINATES);
  return Array.from({ length: 20 }, () => ({
    source: countries[Math.floor(Math.random() * countries.length)] as string,
    destination: countries[
      Math.floor(Math.random() * countries.length)
    ] as string,
    value: Math.floor(Math.random() * 1000),
  }));
}

function getColorForTraffic(value: number): string {
  const intensity = Math.min(value / 1000, 1);
  return `hsl(${200 * (1 - intensity)}, 70%, 50%)`;
}

function formatTrafficValue(value: number): string {
  return `${(value / 100).toFixed(1)}Gbps`;
}
