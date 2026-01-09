import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Progress } from "@/components/ui/progress";
import { 
  Flame, 
  Target, 
  TrendingUp, 
  Calendar,
  Dumbbell,
  Clock,
  ChevronRight 
} from "lucide-react";

export default function DashboardPage() {
  return (
    <div className="space-y-6">
      {/* Welcome Section */}
      <div>
        <h1 className="text-3xl font-bold text-white">Welcome back, Athlete! 👋</h1>
        <p className="text-slate-400 mt-1">Here&apos;s your training overview for today.</p>
      </div>

      {/* Stats Grid */}
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <Card className="border-slate-800 bg-slate-900/50">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-slate-400">Current Streak</CardTitle>
            <Flame className="h-4 w-4 text-orange-500" />
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-white">12 days</div>
            <p className="text-xs text-emerald-400 mt-1">+2 from last week</p>
          </CardContent>
        </Card>

        <Card className="border-slate-800 bg-slate-900/50">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-slate-400">Weekly Goal</CardTitle>
            <Target className="h-4 w-4 text-emerald-500" />
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-white">4/5</div>
            <Progress value={80} className="mt-2 h-2 bg-slate-800" />
          </CardContent>
        </Card>

        <Card className="border-slate-800 bg-slate-900/50">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-slate-400">This Month</CardTitle>
            <TrendingUp className="h-4 w-4 text-blue-500" />
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-white">18</div>
            <p className="text-xs text-slate-400 mt-1">workouts completed</p>
          </CardContent>
        </Card>

        <Card className="border-slate-800 bg-slate-900/50">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-slate-400">Next Workout</CardTitle>
            <Calendar className="h-4 w-4 text-purple-500" />
          </CardHeader>
          <CardContent>
            <div className="text-xl font-bold text-white">Upper Body</div>
            <p className="text-xs text-slate-400 mt-1">Today at 6:00 PM</p>
          </CardContent>
        </Card>
      </div>

      {/* Main Content Grid */}
      <div className="grid gap-6 lg:grid-cols-3">
        {/* Today's Workout */}
        <Card className="lg:col-span-2 border-slate-800 bg-slate-900/50">
          <CardHeader>
            <CardTitle className="text-white">Today&apos;s Workout</CardTitle>
            <CardDescription className="text-slate-400">Upper Body Strength</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            {[
              { name: "Bench Press", sets: "4x8", muscle: "Chest" },
              { name: "Pull-ups", sets: "4x10", muscle: "Back" },
              { name: "Shoulder Press", sets: "3x12", muscle: "Shoulders" },
              { name: "Bicep Curls", sets: "3x15", muscle: "Arms" },
              { name: "Tricep Dips", sets: "3x12", muscle: "Arms" },
            ].map((exercise, i) => (
              <div
                key={i}
                className="flex items-center justify-between rounded-lg border border-slate-800 bg-slate-800/50 p-4"
              >
                <div className="flex items-center gap-4">
                  <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-emerald-500/10">
                    <Dumbbell className="h-5 w-5 text-emerald-400" />
                  </div>
                  <div>
                    <p className="font-medium text-white">{exercise.name}</p>
                    <p className="text-sm text-slate-400">{exercise.muscle}</p>
                  </div>
                </div>
                <div className="flex items-center gap-4">
                  <Badge variant="secondary" className="bg-slate-700 text-slate-300">
                    {exercise.sets}
                  </Badge>
                  <ChevronRight className="h-4 w-4 text-slate-500" />
                </div>
              </div>
            ))}
            <button className="w-full rounded-lg bg-gradient-to-r from-emerald-500 to-cyan-500 py-3 font-semibold text-slate-900 transition-opacity hover:opacity-90">
              Start Workout
            </button>
          </CardContent>
        </Card>

        {/* Quick Stats */}
        <div className="space-y-6">
          {/* Recent Activity */}
          <Card className="border-slate-800 bg-slate-900/50">
            <CardHeader>
              <CardTitle className="text-white">Recent Activity</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              {[
                { workout: "Leg Day", time: "Yesterday", duration: "52 min" },
                { workout: "Cardio HIIT", time: "2 days ago", duration: "30 min" },
                { workout: "Push Day", time: "3 days ago", duration: "48 min" },
              ].map((activity, i) => (
                <div key={i} className="flex items-center justify-between">
                  <div>
                    <p className="text-sm font-medium text-white">{activity.workout}</p>
                    <p className="text-xs text-slate-400">{activity.time}</p>
                  </div>
                  <div className="flex items-center gap-1 text-xs text-slate-400">
                    <Clock className="h-3 w-3" />
                    {activity.duration}
                  </div>
                </div>
              ))}
            </CardContent>
          </Card>

          {/* Goals Progress */}
          <Card className="border-slate-800 bg-slate-900/50">
            <CardHeader>
              <CardTitle className="text-white">Active Goals</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              {[
                { goal: "Bench 225 lbs", progress: 75 },
                { goal: "Run 5K under 25min", progress: 60 },
                { goal: "30 day streak", progress: 40 },
              ].map((item, i) => (
                <div key={i} className="space-y-2">
                  <div className="flex justify-between text-sm">
                    <span className="text-slate-300">{item.goal}</span>
                    <span className="text-slate-400">{item.progress}%</span>
                  </div>
                  <Progress value={item.progress} className="h-2 bg-slate-800" />
                </div>
              ))}
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
}