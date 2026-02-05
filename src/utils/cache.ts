import NodeCache from 'node-cache';
import {ComponentData} from "../typings";

const componentCache = new NodeCache({stdTTL: 3600 * 4.5, checkperiod: 3600 * 4.5});

export const setCache = (key: string, value: any): boolean => {
  return componentCache.set(key, value);
};

export const getCache = (key: string): any => {
  return componentCache.get(key);
};

export const removeCache = (key: string): number => {
  return componentCache.del(key);
};

export const hasKey = (key: string): boolean => {
  return componentCache.has(key)
};
