import { gql } from "@apollo/client";

// ============ QUERIES ============

export const ME_QUERY = gql`
  query Me {
    me {
      id
      email
      username
      role
      bio
    }
  }
`;

export const EXERCISES_QUERY = gql`
  query Exercises {
    exercises {
      id
      name
      description
      difficulty
      muscleGroups
      equipment
    }
  }
`;

export const WORKOUT_TEMPLATES_QUERY = gql`
  query WorkoutTemplates($publicOnly: Boolean!) {
    workoutTemplates(publicOnly: $publicOnly) {
      id
      name
      description
      difficulty
      estimatedDurationMinutes
      isPublic
    }
  }
`;

// ============ MUTATIONS ============

export const LOGIN_MUTATION = gql`
  mutation Login($input: LoginInput!) {
    login(input: $input) {
      id
      email
      username
      role
    }
  }
`;

export const REGISTER_MUTATION = gql`
  mutation Register($input: RegisterInput!) {
    register(input: $input) {
      id
      email
      username
      role
    }
  }
`;

export const LOGOUT_MUTATION = gql`
  mutation Logout {
    logout
  }
`;