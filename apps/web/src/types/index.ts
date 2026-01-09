// User types
export type UserRole = 'athlete' | 'coach' | 'admin';

export interface User {
  id: string;
  email: string;
  username: string;
  role: UserRole;
  avatar?: string;
  bio?: string;
  createdAt: string;
}

// Athlete types
export type ExperienceLevel = 'beginner' | 'intermediate' | 'advanced' | 'elite';

export interface Sport {
  id: string;
  name: string;
  description?: string;
  icon?: string;
}

export interface AthleteProfile {
  id: string;
  user: User;
  sports: Sport[];
  experienceLevel: ExperienceLevel;
  dateOfBirth?: string;
  heightCm?: number;
  weightKg?: number;
  goals?: string;
}

// Workout types
export type Difficulty = 'beginner' | 'intermediate' | 'advanced';

export interface Exercise {
  id: string;
  name: string;
  description?: string;
  instructions?: string;
  muscleGroups: string[];
  equipment: string[];
  difficulty: Difficulty;
  videoUrl?: string;
}

export interface WorkoutExercise {
  id: string;
  exercise: Exercise;
  order: number;
  sets: number;
  reps: string;
  restSeconds: number;
  notes?: string;
}

export interface WorkoutTemplate {
  id: string;
  name: string;
  description?: string;
  exercises: WorkoutExercise[];
  estimatedDurationMinutes: number;
  difficulty: Difficulty;
  isPublic: boolean;
}

// Progress types
export type GoalType = 'strength' | 'endurance' | 'weight' | 'habit' | 'custom';
export type GoalStatus = 'active' | 'completed' | 'abandoned';

export interface Goal {
  id: string;
  title: string;
  description?: string;
  goalType: GoalType;
  targetValue?: number;
  currentValue?: number;
  unit?: string;
  deadline?: string;
  status: GoalStatus;
}

export interface Streak {
  id: string;
  streakType: 'workout' | 'login' | 'goal';
  currentCount: number;
  longestCount: number;
  lastActivityDate?: string;
}