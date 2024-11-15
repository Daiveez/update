; ModuleID = "main"
target triple = "arm64-apple-darwin24.0.0"
target datalayout = ""

define i32 @"main"()
{
main_entry:
  %".2" = alloca i32
  store i32 50, i32* %".2"
  %".4" = alloca i32
  store i32 45, i32* %".4"
  ret i32 69
}
