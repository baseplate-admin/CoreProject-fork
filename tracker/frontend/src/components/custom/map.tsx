import { forwardRef, useEffect, useRef, useImperativeHandle } from "react";
import { Map, MapOptions, MapMouseEvent } from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";

export interface MapLibreProps extends Omit<MapOptions, "container"> {
  className?: string;
  containerStyle?: React.CSSProperties;
  onLoad?: (map: Map) => void;
  onMouseMove?: (map: Map, e: MapMouseEvent) => void;
  onMouseLeave?: (map: Map, e: MapMouseEvent) => void;

  onClick?: (map: Map, e: MapMouseEvent) => void;
  initialViewState?: {
    longitude: number;
    latitude: number;
    zoom: number;
  };
}

export const MapLibre = forwardRef<Map, MapLibreProps>(
  (
    {
      className = "",
      containerStyle,
      onLoad,
      onMouseMove,
      onMouseLeave,
      onClick,
      initialViewState = {
        longitude: 0,
        latitude: 0,
        zoom: 1,
      },
      style: mapStyle = "https://demotiles.maplibre.org/style.json",
      ...mapOptions
    },
    ref,
  ) => {
    const mapContainerRef = useRef<HTMLDivElement>(null);
    const mapRef = useRef<Map | null>(null);

    // Expose map instance via ref
    useImperativeHandle(ref, () => mapRef.current as Map);

    useEffect(() => {
      if (!mapContainerRef.current) return;

      const { longitude, latitude, zoom } = initialViewState;
      const map = new Map({
        container: mapContainerRef.current,
        style: mapStyle,
        center: [longitude, latitude],
        zoom,
        ...mapOptions,
      });

      mapRef.current = map;

      if (onLoad) map.on("load", () => onLoad(map));
      if (onMouseMove) map.on("mousemove", (e) => onMouseMove(map, e));
      if (onClick) map.on("click", (e) => onClick(map, e));

      return () => {
        mapRef.current = null;
        map.remove();
      };
    }, []);

    return (
      <div
        ref={mapContainerRef}
        className={`bg-background h-[400px] w-full rounded-lg border ${className}`}
        style={containerStyle}
        data-testid="map-container"
      />
    );
  },
);

MapLibre.displayName = "MapLibre";
